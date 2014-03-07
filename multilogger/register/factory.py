from formulator.models import Form, FieldSet, Field
from django.utils.translation import ugettext_lazy as _

# FORM1
# =====
form_class = Form(name='sdv_form_en')
form_class.save()

# Composition of a Fieldset
fieldset = FieldSet(form=form_class,
                    name='fieldset1',
                    legend='This is a legend')
fieldset.save()

# Composition of the fields
Field.objects.create(   name="firstname",
                        field="CharField",
                        label=_('Your first name, SDV?'),
                        formset=fieldset
)
Field.objects.create(   name="lastname",
                        field="CharField",
                        label=_('Your last name, SDV?:'),
                        formset=fieldset
)
Field.objects.create(   name="username",
                        field="CharField",
                        attrs={"max_length":"30", "placeholder":"username here"},
                        formset=fieldset
)
Field.objects.create(   name="password",
                        field="CharField",
                        widget='PasswordInput',
                        help_text=_('Make sure to use a secure password.'),
                        formset=fieldset
)

# FORM2
# =====
form_class = Form(name='adce_form_en')
form_class.save()

# Composition of a Fieldset
fieldset = FieldSet(form=form_class,
                    name='fieldset1',
                    legend='This is a legend')
fieldset.save()

# Composition of the fields
Field.objects.create(   name="firstname",
                        field="CharField",
                        label=_('Your first name, ADCE?'),
                        formset=fieldset
)
Field.objects.create(   name="lastname",
                        field="CharField",
                        label=_('Your last name, ADCE?:'),
                        formset=fieldset
)

