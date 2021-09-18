from django.urls import path



from surveysApp import apiviews



app_name = 'surveysApp'
urlpatterns = [
    path('login/', apiviews.login, name='login'),
   
                      ############## Ответ    ###################
    path('answer/create/', apiviews.answer_create, name='СОЗДАТЬ ОТВЕТ'),
    path('answer/view/<int:user_id>/', apiviews.answer_view, name='ПОСМОТРЕТЬ ОТВЕТ'),
    path('answer/update/<int:answer_id>/', apiviews.answer_update, name='ОБНОВИТЬ ОТВЕТ'),
   
                     ############### опросы   #################
    path('surveysApp/create/', apiviews.survey_create, name='СОЗДАТЬ ОПРОС'),
    path('surveysApp/update/<int:survey_id>/', apiviews.survey_update, name='ОБНОВИТЬ ОПРОС'),
    path('surveysApp/view/', apiviews.survey_view, name='ПОСМОТРЕТЬ ОПРОС'),
    path('surveysApp/view/active/', apiviews.active_survey_view, name='ОБНОВИТЬ ОПРОС'),
   
   
                      ############### вопросы  #################
    path('question/create/', apiviews.question_create, name='СОЗДАТЬ ВОПРОС'),
    path('question/update/<int:question_id>/', apiviews.question_update, name='ОБНОВИТЬ ВООПРОС'),
  
  
                      ############### выбор  #################
    path('choice/create/', apiviews.choice_create, name='ВЫБРАТЬ ОТВЕТ'),
    path('choice/update/<int:choice_id>/', apiviews.choice_update, name='ОБНОВИТЬ ОТВЕТ'),
  
  
 
 

 
]

