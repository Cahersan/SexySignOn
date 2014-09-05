-- import the redis and json modules
local redis = require "resty.redis"
-- local JSON = require "resty.JSON"
local cjson = require "cjson"
-- Some variable declarations.
local cookie = ngx.var.cookie_SSOSessionID
local red = redis:new()
local SSO_KEY = "this is a very secret key!"

red:set_timeout(1000) -- 1 sec

-- Check that the cookie exists.
if cookie ~= nil then

    -- Check for redis connection
    local ok, err = red:connect("127.0.0.1", 6379)
    if not ok then
        ngx.say("Failed to connect to Redis Server")
        return
    end

    local coded_session_data, err = red:get(cookie)

    -- The session might have expired while the cookie exists. Check.
    if not coded_session_data then
         ngx.redirect("/login")
    end
    if coded_session_data == ngx.null then
         ngx.redirect("/login")
    end

    -- Session data is stored base64-enconcoded. Decode.
    local decoded_session_data = ngx.decode_base64(coded_session_data)

    -- Get the data in JSON and parse.
    local divider = decoded_session_data:find(":")
    local json_data = decoded_session_data:sub(divider+1)
    local session_data = cjson.decode(json_data)

    -- uuid and user
    local uuid = session_data.uuid
    local user = session_data.user

    -- Creating the signature
    local k =  (uuid .. ":" .. user)
    local digest = ngx.hmac_sha1(SSO_KEY, k)
    local sso_signature = (ngx.encode_base64(digest) .. ":" .. k)
    
    ngx.req.set_header("SSO_UUID", uuid)
    ngx.req.set_header("SSO_USER", user)
    ngx.req.set_header("SSO_SIGNATURE", sso_signature)

    return
end

-- Internally rewrite the URL so that we serve
-- /auth/ if there's no valid token.
ngx.redirect("/login")
