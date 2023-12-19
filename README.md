## Python JSON based Logger
 
## Identifier
Each apllication(web/system/lambda/etc..) will need to have a Unique category as Identifier.
 
## Configuration
Just import `JSONAL` from this file.

```sh
    app = Flask(__name__)
    error_logger = JSONAL(app)
    #call it like this in: 
    error_logger.log_erro(errorvariable)
```
## Author

[slimdestro(Mukul Kumar)](https://linktr.ee/slimdestro)
