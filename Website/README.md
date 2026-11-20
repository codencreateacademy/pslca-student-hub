# Website support files

This folder contains the website pages, styles and release settings. Classroom PDFs, charts and resource READMEs remain in the grade-band and Shared_Resources folders.

GitHub Actions runs `python Website/build.py` and publishes the assembled `_site` folder. The site keeps the same public addresses even though its support files are stored here.

Edit a website page under its matching path here. Add student documents to their normal grade-band or shared-resource folder. The build copies those documents into the published website at their existing paths.

The release settings are at `Website/Shared_Resources/Voltage_Lab/release.json`.
