#!/usr/bin/python3
# -*- coding: utf-8 -*-

# I don't use PyMISP because a lot of :
# ResourceWarning: unclosed <socket.socket fd=5 [.......

## TODO : 
#   make test with differents key
#   add complexity
#   test query level


from keys import testKeys
from dummy_event_serachv2 import evt

# from deepdiff import DeepDiff

import unittest
import requests
import json
import time

urlPath = {
    'scope' : ['attributes'], 
    'V1' : '/restSearch/json/',
    'V2' : '/restSearch2/'
}
# :additional_path list
# :return full url
def url_join(items):
    return "/".join([(u.strip("/") if index + 1 < len(items) else u.lstrip("/")) for index, u in enumerate(items)])

def removeTestEvent(eid, s):
    s.headers.update({'Authorization': testKeys['admin']['key']})
    urlTodelete = url_join([testKeys['admin']['url'], 'events/{}'.format(eid)])
    r = s.delete(urlTodelete)
    s.close() 
    print("Remove : {}".format(eid))

def execSearch(session, tosearch, urlPath):
    r = session.post(urlPath, data=json.dumps(tosearch))
    # print(urlPath)
    # print(session.headers['Authorization'])
    # print(r)
    # print(r.text)
    return json.loads(r.text)

def getAttrsFromTestId(attrs, eid):
    return [attrs[i] for i,attr in enumerate(attrs) if attr['event_id'] == eid]


class TestSearchV2(unittest.TestCase):

    def setUp(self):
        self.session = requests.Session()
        self.session.headers.update(
            {'Authorization': testKeys['admin']['key'],
             'Accept': 'application/json',
             'content-type': 'application/json'})
        urlToPost = url_join([testKeys['admin']['url'], 'events'])
        r = self.session.post(urlToPost, data=json.dumps(evt))
        self.event_id = json.loads(r.text)['Event']['id']
        print("new event created for test : {}".format(self.event_id))
        self.addCleanup(removeTestEvent, self.event_id, self.session)

    def test_search_single_type_1(self):
        # search for type "AS"
        tosearch = {"request" : {"type" : "AS"}}
        print(tosearch)
        # search with different keys
        for mispRole, mispKey in testKeys.items():
            print(mispRole)
            self.session.headers.update({'Authorization': mispKey['key']})
            # look at the difference between V1 and V2
            rv1 = execSearch(
                session=self.session,
                tosearch=tosearch,
                urlPath=url_join([
                    mispKey['url'], 
                    urlPath['scope'][0], #only one for type ^^
                    urlPath['V1']])
            )
            attrsv1 = rv1['response']['Attribute']

            # v1 is not strict, remove other
            attrsv1 = [attrsv1[i] for i,attr in enumerate(attrsv1) if attr['type'] == 'AS']
            attrsv1 = [attrsv1[i] for i,attr in enumerate(attrsv1) if attr['event_id'] == self.event_id]
            rv1['response']['Attribute'] = attrsv1
            # print(json.dumps(attrsv1, indent=4, sort_keys=True))

            # in v2 :
            # valide for : Type, TyPe, [...], attributes.Type
            rv2 = execSearch( 
                session=self.session,
                tosearch=tosearch,
                urlPath=url_join([
                    mispKey['url'], 
                    urlPath['scope'][0], 
                    urlPath['V2']])
            )
            rv2['response']['Attribute'] = getAttrsFromTestId(rv2['response']['Attribute'], self.event_id)
            # self.maxDiff = None
            self.assertDictEqual(rv1, rv2) 


    def test_simple_or(self):
        # don't work in v1
        tosearch = {"request" : {"OR" : [{"type" :["AS", "campaign-name"]}]}}
        print(tosearch)
        for mispRole, mispKey in testKeys.items():
            print(mispRole)
            r = execSearch( 
                    session=self.session,
                    tosearch=tosearch,
                    urlPath=url_join([
                        mispKey['url'], 
                        urlPath['scope'][0], 
                        urlPath['V2']])
                )
            r['response']['Attribute'] = getAttrsFromTestId(r['response']['Attribute'], self.event_id)
            # print(json.dumps(r, indent=4, sort_keys=True))
            for attr in r['response']['Attribute']:
                if attr['type'] == "AS":
                    self.assertEqual(attr['value'], "ResultForAsType")
                if attr['type'] == 'campaign-name':
                    self.assertEqual(attr['value'], "myDummyCampaignName")


        #search for type "AS" or "campaign-name"
        # there is a not list in "OR"
        tosearch = {"request" : {"OR" : {"type" :["AS", "campaign-name"]}}}
        print(tosearch)
        for mispRole, mispKey in testKeys.items():
            print(mispRole)
            self.session.headers.update({'Authorization': mispKey['key']})
            r = execSearch( 
                    session=self.session,
                    tosearch=tosearch,
                    urlPath=url_join([
                        mispKey['url'], 
                        urlPath['scope'][0], 
                        urlPath['V2']])
                )
            r['response']['Attribute'] = getAttrsFromTestId(r['response']['Attribute'], self.event_id)
            # print(json.dumps(r, indent=4, sort_keys=True))
            for attr in r['response']['Attribute']:
                if attr['type'] == "AS":
                    self.assertEqual(attr['value'], "ResultForAsType")
                if attr['type'] == 'campaign-name':
                    self.assertEqual(attr['value'], "myDummyCampaignName")

        tosearch = {"request" : {"OR" : [{"type" :"AS"},{"type": "campaign-name"}]}}
        print(tosearch)
        for mispRole, mispKey in testKeys.items():
            print(mispRole)
            r = execSearch( 
                    session=self.session,
                    tosearch=tosearch,
                    urlPath=url_join([
                        mispKey['url'], 
                        urlPath['scope'][0], 
                        urlPath['V2']])
                )
            r['response']['Attribute'] = getAttrsFromTestId(r['response']['Attribute'], self.event_id)
            # print(json.dumps(r, indent=4, sort_keys=True))
            for attr in r['response']['Attribute']:
                if attr['type'] == "AS":
                    self.assertEqual(attr['value'], "ResultForAsType")
                if attr['type'] == 'campaign-name':
                    self.assertEqual(attr['value'], "myDummyCampaignName")








        # for mispRole, mispKey in testKeys.items():
        #     self.session.headers.update({'Authorization': mispKey['key']})
        #     execSearch(
        #         session=self.session,
        #         tosearch=tosearch,
        #         urlPath=urljoin(mispKey['url'], "attributes/restSearch2")
        #     )
        #     break
        
        #search for type "AS" or "campaign-name"
        #the same but not a list in "OR"
        # tosearch = {"request" : {"OR" : {"type" :["AS", "campaign-name"]}}}
        # for mispRole, mispKey in testKeys.items():
        #     self.session.headers.update({'Authorization': mispKey['key']})
        #     execSearch(
        #         session=self.session,
        #         tosearch=tosearch,
        #         urlPath=urljoin(mispKey['url'], "attributes/restSearch2")
        #     )
        #     break


        # r = execSearchv2(self.session, tosearch, testKeys['admin']['url'], "attributes/restSearch2")
        # self.assertIsNotNone(r)
        # for attr in r['response']:
        #     if attr['Attribute']['event_id'] == self.event_id:
        #         if attr['Attribute']['type'] == "AS":
        #             self.assertEqual(attr['Attribute']['value'], "ResultForAsType")

    # def test_search_type_2(self):
    #     tosearch = {"query" : {"OR" : [{"type" :["AS", "campaign-name"]}]}}
    #     r = execSearchv2(self.session, tosearch)
        # print(r) 

if __name__ == '__main__':
    unittest.main()