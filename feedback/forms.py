#!/usr/bin/env python
from django import forms
from django.contrib.sites.models import Site
from captcha.fields import CaptchaField

import models

class FeedbackForm(forms.ModelForm):
    '''The form shown when giving feedback'''
    captcha = CaptchaField()
    
    class Meta:
        model = models.Feedback
        #exclude = ('site', 'url')

# vim: et sw=4 sts=4
