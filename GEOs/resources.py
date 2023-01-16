from GEOs import resources
from .models import Community
 
class CommunityResource(resources.ModelResource):
    class Meta:
        model = Community