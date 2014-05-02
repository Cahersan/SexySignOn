-- import the redis and json modules
local redis = require "resty.redis"
-- local JSON = require "resty.JSON"
local cjson = require "cjson"
-- Some variable declarations.
local IDCookie = ngx.var.cookie_SSOSessionID
local red = redis:new()
local secret_key = "this is a very secret key!"

red:set_timeout(1000) -- 1 sec

-- Check that the cookie exists.
if IDCookie ~= nil then

    -- check for redis connection
    local ok, err = red:connect("127.0.0.1", 6379)
    if not ok then
        ngx.say("Failed to connect to Redis Server")
        return
    end

    local codedData = red:get(IDCookie)
    local decodedData = ngx.decode_base64(codedData)

    local divider = decodedData:find(":")
    local JSONData = decodedData:sub(divider+1)
    local sData = cjson.decode(JSONData)
    local UUID = sData.uuid

    -- If there's a cookie, check that it is stored in redis
    if not sData.username then
        ngx.redirect("/login")
        return
    end
    
    local digest = ngx.hmac_sha1(secret_key, UUID)
    local SSO_UUID_TOKEN = (ngx.encode_base64(digest) .. ":" .. UUID)
    
    ngx.req.set_header("SSO-PROFILE", JSONData)
    ngx.req.set_header("SSO-UUID", SSO_UUID_TOKEN)
    return
end

-- Internally rewrite the URL so that we serve
-- /auth/ if there's no valid token.
ngx.redirect("/login")
