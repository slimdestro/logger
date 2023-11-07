## JSONAL
#### Generic JSON as Log for Flask
 
## Identifier
Each apllication(web/system/lambda/etc..) will need to have a Unique category as Identifier.
 
## Configuration
Just import `Helper_FlaskPOC_Custom_ErrorLogger` from this file.

```sh
    app = Flask(__name__)
    error_logger = Helper_FlaskPOC_Custom_ErrorLogger(app)
    #call it like this in: 
    error_logger.log_erro(errorvariable)
```
## Author

[slimdestro(Mukul Kumar)](https://linktr.ee/slimdestro)
