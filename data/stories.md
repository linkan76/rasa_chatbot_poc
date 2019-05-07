## greet
* greet
    - utter_greet

## thank
* thank
    - utter_thank

## bye
* bye
    - utter_bye

## ask_jenkinsjob
	- utter_ask_jenkinsjob

## trigger_jenkinsjob
* trigger_jenkinsjob
	- utter_ask_jenkinsjob
* information_jenkinsjob{"jenkinsjob": "sampleapp_ppl"}
    - action_jenkins
	
## trigger_jenkinsjob
* greet
    - utter_greet
* trigger_jenkinsjob
	- utter_ask_jenkinsjob
* information_jenkinsjob{"jenkinsjob": "sampleapp_ppl"}
    - action_jenkins
	
## trigger_jenkinsjob
* greet
    - utter_greet
* trigger_jenkinsjob
	- utter_ask_jenkinsjob
* information_jenkinsjob
	- action_jenkins
	- slot{"jenkinsjob": "sampleapp_ppl"}

## trigger_jenkinsjob_withjob
* trigger_jenkinsjob_withjob{"jenkinsjob": "sampleapp_ppl"}
	- slot{"jenkinsjob": "sampleapp_ppl"}
    - action_jenkins
* bye
    - utter_anythingelse
	
## trigger_deploy
* trigger_deploy
	- utter_ask_appname
	- utter_ask_environment
* anythingelse
    - utter_anythingelse

## trigger_deploy_withapp
* trigger_deploy_withapp{"appname": "sampleapp"}
    - action_jenkins_param
* anythingelse
    - utter_anythingelse

## check_service
* check_service
	- utter_ask_service
* anythingelse
    - utter_anythingelse
	
## check_service_withservice1
* check_service_withservice{"servicename": "google"}
    - action_checkservice
* anythingelse
    - utter_anythingelse
	

