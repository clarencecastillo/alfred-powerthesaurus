# Power Thesaurus Search for Alfred #

Search for synonyms and antonyms on [Power Thesaurus](https://www.powerthesaurus.org) from [Alfred 4](https://www.alfredapp.com/).

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

## Troubleshooting ##

#### SSL Errors
If you're having SSL issues, try temporarily disabling it by setting the workflow environment variable `ALFRED_PT_SSL_VERIFICATION` to `False`. This will bypass SSL verification as a workaround while waiting for the SSL certificate to be rectified. You can check Power Thesaurus's SSL certificate status [here](https://www.sslshopper.com/ssl-checker.html#hostname=api.powerthesaurus.org). Be sure to set it back to `True` when all's green.

#### Other Errors
For other errors, please open an issue describing how you got the error and together with the logs from `Alfred > Workflows > Debugging Mode` if possible. There's no proper error handling in place yet, so we'll have to troubleshoot things this way for now.


## Related Links ##

[GitHub Repository](https://github.com/clarencecastillo/alfred-powerthesaurus)
[Alfred Forums](https://www.alfredforum.com/topic/10576-powerthesaurus-search/)
[Packal](http://www.packal.org/workflow/powerthesaurus-search)

## Releases ##

There's probably a smarter way to do this, but when preparing a new release, don't forget to:

1. Bump `version` file
2. Bump the exported workflow following the format `PowerThesaurus-x.x.x.alfredworkflow`
3. Bump `alfredworkflow.version` field in `metadata.json` or just re-export the entire `metadata.json` from `Alfred > Workflows`

## Licensing ##

This workflow is released under the [MIT Licence](http://opensource.org/licenses/MIT).

By using this workflow, you acknowledge, understand and signify your agreement to Power Thesaurus Website's [terms and conditions](https://www.powerthesaurus.org/_terms_conditions), and [privacy statement](https://www.powerthesaurus.org/_privacy_statement).

## Acknowledgements ##

Big shoutout to the heroes that made Power Thesaurus possible. Help keep the platform free for everyone by [giving your support](https://www.powerthesaurus.org/_about).

It is heavily based on [deanishe's](https://github.com/deanishe) [Alfred-Workflow](http://www.deanishe.net/alfred-workflow/), also
[MIT-licensed](http://opensource.org/licenses/MIT).
