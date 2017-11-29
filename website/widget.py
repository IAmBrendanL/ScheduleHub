from django.forms.widgets import MultiWidget, Select


class DateTime(MultiWidget):
    def __init__(self, atters=None):
        hours = (
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'),
        ('10', '10'), ('11', '11'), ('12', '12'))
        minutes = (('00', '00'), ('15', '15'), ('30', '30'), ('45', '45'))
        daySplit = (('AM', 'AM'), ('PM', 'PM'))

        widgets = (
            Select(choices=hours),
            Select(choices=minutes),
            Select(choices=daySplit),
        )
        super(DateTime, self).__init__(widgets, atters)

    def decompress(self, value):
        if value:
                return [value.hour, value.minute, value.AMPM]
        return [None, None, None]

    def format_output(self, rendered_widgets):
        return u''.join(rendered_widgets)