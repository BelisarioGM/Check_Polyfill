# polyfill.js Detection Script

## Context
The `polyfill.js` is a popular open source library designed to support older browsers. Over 100,000 sites embed it using the `cdn.polyfill.io` domain. Notable users include JSTOR, Intuit, and the World Economic Forum. However, in February this year, a Chinese company acquired the domain and the GitHub account associated with `polyfill.js`. Since then, this domain has been caught injecting malware into mobile devices via any site that embeds `cdn.polyfill.io`.

## Description
This script checks if a given website uses the `polyfill.js` library. It does this by scanning the HTML content of the website and looking for script tags that include `polyfill.js`.

## Prerequisites
Before running the script, you need to install the required dependencies. These dependencies are listed in the `requirements.txt` file.

## Installation

1. Clone the repository or download the script to your local machine.
2. Ensure you have Python installed on your system.
3. Install the required Python packages using the following command:

    ```bash
    pip install -r requirements.txt
    ```

## Usage
To use the script, run it from the command line with the `-u` flag followed by the URL of the website you want to check.

```bash
python check_polyfill.py -u http://example.com
