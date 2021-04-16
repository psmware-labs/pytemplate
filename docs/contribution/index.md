---
 sort: 999
---
# Contributing

Thanks for your consideration to contribute to our documentation!
This repository is built with [Jekyll](https://jekyllrb.com/) so most of their documentation is helpful and
valid for this repository too.

## Publishing sources for GitHub Pages sites

The publishing source for your GitHub Pages site is the branch and folder where the source files for your site are stored.

```warning
**Warning:** GitHub Pages sites are publicly available on the internet by default, even if the repository for the site is private. If you have sensitive data in your site's repository, you may want to remove the data before publishing.
```

It is recommended that you publish your site from any branch in the repository, from the /docs folder on that branch. For more information, see [Configuring a publishing source for your GitHub Pages site.](https://docs.github.com/en/github/working-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#choosing-a-publishing-source)

GitHub Pages will read everything to publish your site, from the `/docs` folder.

## Rules

1. Create new folders and files on first level of repository structure for new documentation
1. Use [kebab-case](https://en.wikipedia.org/wiki/Letter_case#Special_case_styles) for the folder and file names
1. If provided and reasonable please use templates to create new documents.
1. when creating a folder, if you wish the folder to appear in the navigation tree on the left hand side navigation, you must include an `index.md` file containing a title and sort order, i.e.

An example `index.md` is as follows

```markdown
---
 sort: 999
---
# My New Folder

{% include list.liquid all=true %}

```

and would be used as follows:

```markdown
my-new-folder
├─ index.md (This is the file that contains the section header and order for listing in the navbar)
├─ my-new-sub-folder (this folder contains moreall documentation pages)
│ ├─ index.md (This is the file that contains the section header and order for listing in the navbar)
│ ├─ 1-subfolder-level-document.md
│ ├─ 2-subfolder-level-document.md
│ ├─ 3-subfolder-level-document.md
│ └─ 4-subfolder-level-document.md
├─ top-level-document.md
└─ another-top-level-document.md
```
