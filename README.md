# chart_parser_api
This API parsing information from spotify chart. 

This API based on django and DRF. 
For parsing information it using Scrapy framework parser.

## USAGE
For parse actual data you need to manage command through the CMD by next command:
- python manage.py load_data

To get chart list use:
- api/chart/ (Get list of songs)
- api/chart/<str:author>/ (Get song detail info by author name)
