MadeiraCloud HTML5 IDE Documents
========
## Theme
You can customise your theme base on the init theme

1. `cp -a ./themes/init ./themes/yourthemename`
2. Edit the CSS or HTML,  Add image in the static folder
3. Set `html_theme = 'yourthemename'` in conf.py


## Build
Just run `make` command in project root folder. Then the document will build to `_build/html` folder and you must test it before deploy


## Deploy
Run `make deploy` to deploy project on [GitHubPage](http://madeiracloud.github.io/h5-docs/) and [ReadTheDocs](http://madeiracloud-document.readthedocs.org/en/latest/)

## Changelog

- 2013-09-29 First Release.

## Links

- [MadeiraCloud HTML5 IDE](https://ide.madeiracloud.com/v2/)

- [Document on GitHub Page](http://madeiracloud.github.io/h5-docs/)

- [Document on ReadtheDocs](http://madeiracloud-document.readthedocs.org/en/latest/)
