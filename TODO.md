# TODO

## 2023-01-19
 1. change project name to "opendatadm"
 2. change directory structure <code folder>/<project folder>/<app folder> , eg. "opendatadm/opendatadm/geos"
 3. create separate app for APIs, and place within "geos" directory, eg. "opendatadm/opendatadm/geos/apis/v202301"
 4. switch to using class based generic list view for API views
 5. enable pagination on list views
 6. remove trailing spacing on end points
 7. add version number to end-point URLs, eg. "/geos/v202301/communities"
 8. add welcome/index page/view to API, eg. "geos/v202301/"
 9. change title of API in browser mode from default of "Django Rest Framework" to "Geos (v202301)"
 10. add API keys
 11. add rate limits (to DRF)
 12. Use [Nested Relations](https://www.django-rest-framework.org/api-guide/relations/#nested-relationships) to the `Community` serializer
 13. allow non-API key based access when in dev mode
 14. add app namespacing to app level `urls.py
 15. install and setup `flake8` for project
 16. create a "data" directory, and move database into it

## 2023-01-18
 1. title/proper case all model names within admin **COMPLETED**
 2. sort community type by name (only within admin) **COMPLETED**
 3. fix pluralization of "community" of model - added "verbose_name_plural" to class meta.**COMPLETED**
 4. fix pluralization of "parish" of model - added "verbose_name_plural" to class meta.**COMPLETED**
 5. add "code" column to "parish" list in admin **COMPLETED**
 6. add "parish" column to "community" list in admin **COMPLETED**
 7. sort community by name (only within admin) **COMPLETED**
 8. sort parish by name (only within admin) **COMPLETED**
 9. ~~load "CommunityType" separately, then "Parish", then "Community", sorting each by name before loading~~
 10. put entire loading of file into a database transaction **COMPLETED**
 11. ~~use django-ulid for model primary keys~~
 12. add "type" column to community list in "admin" **COMPLETED**
 13. change admin-title from django administration to GEOS **COMPLETED**
 14. create end points to list out data for each model **COMPLETED**