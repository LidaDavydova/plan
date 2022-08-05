from import_export import resources
from .models import Bying
from import_export.fields import Field

class ByingResource(resources.ModelResource):
    published = Field(attribute='sell', column_name='Селлер')
    published1 = Field(attribute='site', column_name='Сайт')
    published2 = Field(attribute='phact', column_name='Факт, %')
    published3 = Field(attribute='plan', column_name='План, %')
    published4 = Field(attribute='procent', column_name='%')
    class Meta:
        model = Bying
        fields = ('Селлер', 'Сайт', 'Факт, %', 'План, %', '%')