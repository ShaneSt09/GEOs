1. title/proper case all model names within admin ***
2. sort community type by name (only within admin) ***
3. fix pluralization of "community" of model - added "verbose_name_plural" to class meta.***
4. fix pluralization of "parish" of model - added "verbose_name_plural" to class meta.***
5. add "code" column to "parish" list in admin ***
6. add "parish" column to "community" list in admin ***
7. sort community by name (only within admin) ***
8. sort parish by name (only within admin) ***
9. load "CommunityType" separately, then "Parish", then "Community", sorting each by name before loading
10. put entire loading of file into a database transaction ***
11. use django-ulid for model primary keys ***
12. add "type" column to community list in "admin" ***
13. change admin-title from django administration to GEOS ***

14. create end points to list out data for each model