from django.db import models
from dj_jsonfield.fields import JSONField


class JSONFieldTestModel(models.Model):
    json = JSONField("test", null=True, blank=True)

    class Meta:
        app_label = 'dj_jsonfield'


class JSONFieldWithDefaultTestModel(models.Model):
    json = JSONField(default={"sukasuka": "YAAAAAZ"})

    class Meta:
        app_label = 'dj_jsonfield'


class BlankJSONFieldTestModel(models.Model):
    null_json = JSONField(null=True)
    blank_json = JSONField(blank=True)

    class Meta:
        app_label = 'dj_jsonfield'


class CallableDefaultModel(models.Model):
    json = JSONField(default=lambda: {'x': 2})

    class Meta:
        app_label = 'dj_jsonfield'
