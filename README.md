# Linux Academy Flashcards to Anki Flashcards
This repo is so we can turn the LinuxAcademy.com Flashcards into Anki Flashcards!
Use the Chrome developer tools to get the JSON (or a curl command to get the JSON) then run it through this script!

## Getting started
With the Chrome developer tools open, go to network tab, then browse to the flashcards you'd like to copy. Either copy/save the JSON contents or right click and get a curl command to just download the json directly. Then use that JSON file with the included script.

### To Do
Currently you need to edit the file path in the script. That will change once I implement the click library and make this a real CLI tool

## Acknowledgements
* waf for making some code I could basically just steal and modify (https://github.com/waf/anki-thai/)
