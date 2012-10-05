### PSF Outreach Blog

#### How to

* pip install -r requirements.txt
* create posts in `/content` of master branch
* create pages in `/pages` of master branch
* add images to `/images` of master branch

Once ready to publish:
* Run `$ pelican -s orig_publishconf.py`
* Run `$ ghp-import output`
* Run `$ git push orign gh-pages`

New content should be push to site nearly immediately.