from formulator.models import Form, FieldSet, Field
from django.utils.translation import ugettext_lazy as _

# FORM1
# =====
form_class = Form(name='adce jury registration')
form_class.save()

# Composition of a Fieldset
fieldset = FieldSet(form=form_class,
                    name='fieldset1',
                    legend='This is a legend')
fieldset.save()

# Composition of the fields
Field.objects.create(   name="firstname",
                        field="CharField",
                        label=_('Your first name, ADCE jury?'),
                        formset=fieldset
)
Field.objects.create(   name="lastname",
                        field="CharField",
                        label=_('Your last name, ADCE jury?:'),
                        formset=fieldset
)
Field.objects.create(   name="country",
                        field="CharField",
                        attrs={"max_length":"30", "placeholder":"country here"},
                        formset=fieldset
)

# FORM2
# =====
form_class = Form(name='adce submitter registration')
form_class.save()

# Composition of a Fieldset
fieldset = FieldSet(form=form_class,
                    name='fieldset1',
                    legend='This is a legend')
fieldset.save()

# Composition of the fields
Field.objects.create(   name="firstname",
                        field="CharField",
                        label=_('Your first name, ADCE submitter?'),
                        formset=fieldset
)
Field.objects.create(   name="lastname",
                        field="CharField",
                        label=_('Your last name, ADCE submitter?:'),
                        formset=fieldset
)

