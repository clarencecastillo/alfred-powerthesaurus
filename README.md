# Powerthesaurus Search for Alfred #

Search for synonyms and antonyms on [Powerthesaurus.org](https://www.powerthesaurus.org) from [Alfred 4](https://www.alfredapp.com/).

![](demo.gif "")

## Installation ##

Get Power Thesaurus for Alfred from [GitHub](https://github.com/clarencecastillo/alfred-powerthesaurus/releases) or [Packal](http://www.packal.org/workflow/powerthesaurus-search).

## Usage ##

Primary commands:
- `pows <word>` — Search Power Thesaurus for synonyms of `<word>`.
- `powa <word>` — Search Power Thesaurus for antonyms of `<word>`.

For both primary commands:
  - `↩` or ` ⌘+C` — Copy highlighted entry to the clipboard
  - `⌘+L` — Show full query in Alfred's Large Text window
  - `⌘+↩` — Open highlighted entry in browser
  - `SHIFT` — Preview highlighted entry's page using quicklook

## Results ##

Resulting synonyms or antonyms will be sequentially listed according to user rating.

## Development ##

Use the `init.sh` script to install the required dependencies inside the `src` folder. When you're ready to test or export, copy the entire `src` folder to the existing workflow directory.

## Releases ##

When preparing a new release, don't forget to:

1. Bump `version` file
2. Update `user-agent` version inside `src/api.py` (hopefully the devs will appreciate this)
3. Update the exported workflow following the format `Powerthesaurus-x.x.x.alfredworkflow`


## Licensing ##

This workflow is released under the [MIT Licence](http://opensource.org/licenses/MIT).

By using this workflow, you acknowledge, understand and signify your agreement to Power Thesaurus Website's [terms and conditions](https://www.powerthesaurus.org/_terms_conditions), and [privacy statement](https://www.powerthesaurus.org/_privacy_statement).

## Acknowledgements ##

Big shoutout to the heroes that made Power Thesaurus possible. Help keep the platform free for everyone by [giving your support](https://www.powerthesaurus.org/_about).

It is heavily based on [deanishe's](https://github.com/deanishe) [Alfred-Workflow](http://www.deanishe.net/alfred-workflow/), also
[MIT-licensed](http://opensource.org/licenses/MIT).
