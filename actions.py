from rasa_core.actions import Action
from rasa_core_sdk.events import SlotSet
import httplib2



class ActionCheckService(Action):

    def name(self):
        # you can then use action_example in your stories
        return "action_checkservice"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        s=str(tracker.get_slot("servicename"))
        URL="https://www."+s+".com"
        try:
            resp, content = httplib2.Http().request(URL)
            if resp.status==200:
                response="""{} is up and running  """.format(URL)
                dispatcher.utter_message(response)
            elif resp.status==302:
                response="""{} is up and running  """.format(URL)
                dispatcher.utter_message(response)
            else:
                dispatcher.utter_message("Errorcode :"+str(resp.status)+" For website:"+URL)
        except:
            dispatcher.utter_message("Sorry! an exception occured in accessing "+s+" website")
        return []


class ActionStartJenkinsBuild(Action):

    def name(self):
        # you can then use action_example in your stories
        return "action_jenkins"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        job=str(tracker.get_slot('jenkinsjob'))
        #job = str(tracker.get_slot('jenkinsjob'))
        URL='http://localhost:8080/job/' + job \
            + '/build?token=remote_enable_token'
        dispatcher.utter_message('URL :' + URL)
        try:
            (resp, content) = httplib2.Http().request(URL)
            if resp.status == 201:
                response = 'Job successfully triggered'
                dispatcher.utter_message(response)
                dispatcher.utter_message(str(content.decode('utf-8')))
            else:
                dispatcher.utter_message('status code :'
                        + str(resp.status))
                dispatcher.utter_message(content.decode())
        except:
            dispatcher.utter_message('Sorry! an exception occured in triggering the job'
                    )
        return []


        
class ActionStartJenkinsBuildWithParams(Action):
    def name(self):
        return "action_jenkins_param"

    def run(self, dispatcher, tracker, domain):
        job = str(tracker.get_slot("appname"))
#        if(tracker.get_slot("param")=="environment"):
#            param = "Environment"
        pvalue = str(tracker.get_slot("environment")).upper()
        URL = "http://localhost:8080/job/"+job+"/buildWithParameters?token=remote_enable_token&Environment="+pvalue
        dispatcher.utter_message("URL :" + URL)
        try:
            resp, content = httplib2.Http().request(URL)
            if resp.status==201:
                response="Job successfully triggered with "+param+"="+pvalue
                dispatcher.utter_message(response)
            else:
                dispatcher.utter_message("status code :"+str(resp.status))
                dispatcher.utter_message(content.decode())
        except:
            dispatcher.utter_message("Sorry! an exception occured in triggering the job")
        return []        

class ActionRequestAccess(Action):

    def name(self):
        # you can then use action_example in your stories
        return "action_request_access"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        job=str(tracker.get_slot('access'))
        #job = str(tracker.get_slot('jenkinsjob'))
        try:
            if job == "ucdprod":
                response = 'Sailpoint request has been raised on your behalf, You will be notified in the email once it is approved'
                dispatcher.utter_message(response)
                dispatcher.utter_message(str(content.decode('utf-8')))
            elif job == "github":
                response = 'Validation completed...You are authorized for access'
                dispatcher.utter_message(response)
                response1 = 'Access has been granted, please validate URL : http://github.mycomp.com/'
                dispatcher.utter_message(response1)
                dispatcher.utter_message(str(content.decode('utf-8')))
            elif job == "svn":
                response = 'Validation completed...You are authorized for access'
                dispatcher.utter_message(response)
                response1 = 'Please contact your Manager.'
                dispatcher.utter_message(response1)
                response1 = dispatcher.utter_message(response1)
                dispatcher.utter_message(str(content.decode('utf-8')))
            elif job == "servicedesk":
                response = 'Access has been granted, please validate URL : http://myservicedesk.mycomp.com/'
                dispatcher.utter_message(response)
                dispatcher.utter_message(str(content.decode('utf-8')))
            else:
                dispatcher.utter_message('Access is not automated through DevOps bot for tool:'
                        + str(job))
        except:
            dispatcher.utter_message('Thanks'
                    )
        return []
