# Power Thesaurus Search for Alfred #

Ported to ALfred 5 and Python 3 from the original version by [@clarencecastillo](https://github.com/clarencecastillo)

----
<a href="https://github.com/giovannicoppola/alfred-powerthesaurus/releases/latest/">
  
  <img alt="Downloads"
       src="https://img.shields.io/github/downloads/giovannicoppola/alfred-powerthesaurus/total?color=purple&label=Downloads"><br/>
</a>



Search for synonyms and antonyms on [Power Thesaurus](https://www.powerthesaurus.org) from [Alfred 4](https://www.alfredapp.com/).

![](demo.gif "")

## Installation ##

Get Power Thesaurus for Alfred from [GitHub](https://github.com/giovannicoppola/alfred-powerthesaurus/releases).

Version 3.1 is for Alfred 5. Use [version 3.0](https://github.com/giovannicoppola/alfred-powerthesaurus/releases/tag/v3.0) for Alfred 4

## Usage ##

Primary commands:
- `pows <word>` — Search Power Thesaurus for synonyms of `<word>`.
- `powa <word>` — Search Power Thesaurus for antonyms of `<word>`.

For both primary commands:
  - `↩` or ` ⌘+C` — Copy highlighted entry to the clipboard
  - `⌘+L` — Show full query in Alfred's Large Text window
  - CMD+enter (⌘↩️) opens synonyms in browser
  - CTRL+enter (^↩️) opens antonyms in browser
  - `SHIFT` — Preview highlighted entry's page using quicklook

## Results ##

Resulting synonyms or antonyms will be sequentially listed according to user rating.


## Troubleshooting ##

#### SSL Errors
If you're having SSL issues, try temporarily disabling it by setting the workflow environment variable `ALFRED_PT_SSL_VERIFICATION` to `False`. This will bypass SSL verification as a workaround while waiting for the SSL certificate to be rectified. You can check Power Thesaurus's SSL certificate status [here](https://www.sslshopper.com/ssl-checker.html#hostname=api.powerthesaurus.org). Be sure to set it back to `True` when all's green.

#### Other Errors
For other errors, please open an issue describing how you got the error and together with the logs from `Alfred > Workflows > Debugging Mode` if possible. There's no proper error handling in place yet, so we'll have to troubleshoot things this way for now.


## Related Links ##

[Alfred Forums](https://www.alfredforum.com/topic/10576-powerthesaurus-search/)

## Releases ##
### November 2022 update (Version 3.1)
- migration to Alfred 5

### March 2022 update (Version 3.0)

- migration to Python 3
- caching eliminated - performance (for cached items) went from ~0.06-0.12 to ~0.4-0.5 secs per query
- now opens both antonyms (CTRL) and synonyms (CMD) in browser


## Licensing ##

This workflow is released under the [MIT Licence](http://opensource.org/licenses/MIT).

By using this workflow, you acknowledge, understand and signify your agreement to Power Thesaurus Website's [terms and conditions](https://www.powerthesaurus.org/_terms_conditions), and [privacy statement](https://www.powerthesaurus.org/_privacy_statement).

## Acknowledgements ##

Big shoutout to the heroes that made Power Thesaurus possible. Help keep the platform free for everyone by [giving your support](https://www.powerthesaurus.org/_about).

It is heavily based on [deanishe's](https://github.com/deanishe) [Alfred-Workflow](http://www.deanishe.net/alfred-workflow/), also
[MIT-licensed](http://opensource.org/licenses/MIT).
