# Website with users articles  
###### First django project from "Python developer" course in programming school "IT technologies itProger"  

## In the site realised blog with users articles:  

- ### Users articles.  

Every registered user can add articles on the site which would displaying on /articles/ page of website. Article sorted by last created. If you push on the author of the article you will see all his articles. If you push on the "read more" ("Читать далее") button you will move to the article's page. Each article has individual url. If author would be deleted from the User database all his articles will be deleted.

- ### Profile, registration, authorisation and password recovery.  

Site has a realisation of these functions. On the profile page user could change his data. If you want that works the password recovery function, you got to change the variables in `settings.py` (that displaying below) on yours.  

``
EMAIL_USE_TLS = True  
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_HOST_USER = 'mezorservice123@gmail.com'  
EMAIL_HOST_PASSWORD = 'dsfasdgdfafdss'  
EMAIL_PORT = 587  
``

- ### Feedback.  

Site has a realisation of this function. Each guest or user could send feedback message `/feedback/` If you want that works the feedback function, you got to change the variables in `settings.py` (that displaying below) on yours.  

``
EMAIL_USE_TLS = True  
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_HOST_USER = 'mezorservice123@gmail.com'  
EMAIL_HOST_PASSWORD = 'dsfasdgdfafdss'  
EMAIL_PORT = 587  
``

## On the website were used:
- Fonts: "Ubuntu" from https://fonts.google.com/ .
- Styles: "Bootstrap4" and own-styles.

###### Creator: Dmitry Shelukhin

### P.S.

Many thanks to Georgy Dudar and programming school "IT technologies itProger" for learning and experience.
