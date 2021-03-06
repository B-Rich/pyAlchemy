'''
Created on Jan 31, 2014
@author: Debanjan Mahata
@contact: email: dxmahata@ualr.edu
'''

from __future__ import print_function
from alchemyapi import AlchemyAPI
import json
import AlchemyStructure


class EntityExtraction:
    """class for extracting entities returned by AlchemyAPI call"""
    
    def __init__(self):
        """Constructor for EntityExtraction class"""
        self.entitiesFromText = [] #list for containing the extracted entities from a given text
        self.entitiesFromUrl = [] #list for containing the extracted entities from a given Url

    
    def extractNamedEntitiesFromText(self,txt):
        """method for extracting named entities from given text"""
        
        #creating AlchemyAPI object
        alchemyapi = AlchemyAPI()
        
        #requesting json response from AlchemyAPI server
        response = alchemyapi.entities('text',txt, { 'sentiment':1 })
        
        
        if response['status'] == 'OK':
                
                for entity in response['entities']:
                    #entity object for storing the properties of an entity
                    entityObj = AlchemyStructure.Entity()
                    
                    #sentiment object for storing the sentiment properties related to an entity
                    sentimentObj = AlchemyStructure.Sentiment()
                    
                    #extracting the name of the entity
                    entityObj.setName(entity['text']) 
                    
                    #extracting the type of the entity example Organization, Person, FieldTerminology ect
                    entityObj.setType(entity['type'])
                    
                    #extracting the relevance of the entity for the particular type
                    entityObj.setRelevance(entity['relevance'])
                    
                    
                    
                    #extracting the type of the sentiment associated with the entity -> positive, negative or neutral
                    sentimentObj.setType(entity['sentiment']['type'])
                    
                    #extracting the score of the sentiment associated with the entity
                    if entity['sentiment']['type'] == "neutral":
                        sentimentObj.setScore("0")
                    else:
                        sentimentObj.setScore(entity["sentiment"]["score"])
                        
                        
                    #extracting the frequency of occurrence of the entity in the given text
                    entityObj.setFreq(entity['count'])
                    
                    #setting the sentiment attached with the entity
                    entityObj.setSentiment(sentimentObj)
                    
                    #insert the entity into the list of retrieved entities
                    self.entitiesFromText.append(entityObj)

        else:
            print('Error in entity extraction call: ', response['statusInfo'])
    
       
    def getNamedEntitiesFromText(self,txt):
        """method for returning the extracted named entities from given text"""
        self.extractNamedEntitiesFromText(txt)
        return self.entitiesFromText
    
    
    def extractNamedEntitiesFromUrl(self,url):
        """method for extracting named entities from given url"""
        
        #creating AlchemyAPI object
        alchemyapi = AlchemyAPI()
        
        #requesting json response from AlchemyAPI server
        response = alchemyapi.entities('url',url, { 'sentiment':1 })
        
        if response['status'] == 'OK':
                
                for entity in response['entities']:
                    #entity object for storing the properties of an entity
                    entityObj = AlchemyStructure.Entity()
                    
                    #sentiment object for storing the sentiment properties related to an entity
                    sentimentObj = AlchemyStructure.Sentiment()
                    
                    #extracting the name of the entity
                    entityObj.setName(entity['text']) 
                    
                    #extracting the type of the entity example Organization, Person, FieldTerminology ect
                    entityObj.setType(entity['type'])
                    
                    #extracting the relevance of the entity for the particular type
                    entityObj.setRelevance(entity['relevance'])
                    
                    #extracting the score of the sentiment associated with the entity
                    if entity['sentiment']['type'] == "neutral":
                        sentimentObj.setScore("0")
                    else:
                        sentimentObj.setScore(entity["sentiment"]["score"])
                    
                    #extracting the type of the sentiment associated with the entity -> positive, negative or neutral
                    sentimentObj.setType(entity['sentiment']['type'])
                    
                    #extracting the frequency of occurrence of the entity in the given text of the url
                    entityObj.setFreq(entity['count'])
                    
                    #setting the sentiment attached with the entity
                    entityObj.setSentiment(sentimentObj)
                    
                    #insert the entity into the list of retrieved entities
                    self.entitiesFromUrl.append(entityObj)

        else:
            print('Error in entity extraction call: ', response['statusInfo'])
        
    
    def getNamedEntitiesFromUrl(self,url):
        """method for returning the extracted named entities from given url"""
        self.extractNamedEntitiesFromUrl(url)
        return self.entitiesFromUrl


class ConceptExtraction:
    """class for extracting concepts returned by AlchemyAPI call"""
    def __init__(self):
        """constructor for ConceptExtraction class"""
        self.conceptsFromText = [] #list of concepts extracted from text
        self.conceptsFromUrl = [] #list of concepts extracted from Url


    def extractConceptFromText(self,txt):
        """method for extracting concepts from given text"""
        
        #creating AlchemyAPI object
        alchemyapi = AlchemyAPI()
              
        #requesting json response from AlchemyAPI server
        response = alchemyapi.concepts('text',txt)
        
        if response['status'] == 'OK':
    
            
            for concept in response['concepts']:
                
                #concept object for storing the extracted concept
                conceptObj = AlchemyStructure.Concept()
                
                #extracting the concept name
                conceptObj.setText(concept['text'])
                
                #extracting the relevance of the concept
                conceptObj.setRelevance(concept['relevance'])
                
                #append the concept into the list of retrieved concepts
                self.conceptsFromText.append(conceptObj)

        else:
            print('Error in concept tagging call: ', response['statusInfo'])
    
    
    def getConceptsFromText(self,txt):
        """method for returning the extracted concepts from given text"""
        self.extractConceptFromText(txt)
        return self.conceptsFromText
    
    
    
    def extractConceptFromUrl(self,url):
        
        """method for extracting concepts from given url"""
        
        #creating AlchemyAPI object
        alchemyapi = AlchemyAPI()
              
        #requesting json response from AlchemyAPI server
        response = alchemyapi.concepts('url',url)
        
        if response['status'] == 'OK':
    

            for concept in response['concepts']:
                
                #concept object for storing the extracted concept
                conceptObj = AlchemyStructure.Concept()
                
                #extracting the concept name
                conceptObj.setText(concept['text'])
                
                #extracting the relevance of the concept
                conceptObj.setRelevance(concept['relevance'])
                
                #append the concept into the list of retrieved concepts
                self.conceptsFromUrl.append(conceptObj)

        else:
            print('Error in concept tagging call: ', response['statusInfo'])
    
    
    
    def getConceptsFromUrl(self,url):
        """method for returning the extracted concepts from given url"""
        self.extractConceptFromUrl(url)   
        return self.conceptsFromUrl
 
 
class KeywordExtraction:
    """class for extracting keywords returned by AlchemyAPI call"""
    def __init__(self):
        self.keywordsFromText = [] #list for containing the keywords extracted from text
        self.keywordsFromUrl = [] #list for containing the keywords extracted from a Url
        
    
    def extractKeywordsFromText(self,txt):
        
        """method for extracting keywords from given text"""
        
        #creating AlchemyAPI object
        alchemyapi = AlchemyAPI()
              
        #requesting json response from AlchemyAPI server
        response = alchemyapi.keywords('text', txt, {'sentiment':1})
        
        if response['status'] == 'OK':
    

            for keywords in response['keywords']:
                
                #concept object for storing the extracted concept
                keyword = AlchemyStructure.Keyword()
                
                #extracting the keyword
                keyword.setText(keywords['text'])
                
                #extracting the relevance of keyword
                keyword.setRelevance(keywords['relevance'])
                
                #instantiating the sentiment object 
                sentimentObj = AlchemyStructure.Sentiment()
                
                #extracting the score of the sentiment associated with the keyword
                if keywords['sentiment']['type'] == "neutral":
                    sentimentObj.setScore("0")
                else:
                    sentimentObj.setScore(keywords["sentiment"]["score"])
                
                #extracting the type of the sentiment associated with the keyword -> positive, negative or neutral
                sentimentObj.setType(keywords['sentiment']['type'])

                #set the sentiment for keyword
                keyword.setSentiment(sentimentObj)
                
                #append the concept into the list of retrieved concepts
                self.keywordsFromText.append(keyword)

        else:
            print('Error in keyword tagging call: ', response['statusInfo'])
            
    
    
    def getKeywordsFromText(self,txt):
        """method for returning the extracted keywords from given url"""
        self.extractKeywordsFromText(txt)
        return self.keywordsFromText

    
    def extractKeywordsFromUrl(self,url):
        """method for extracting keywords from given text"""
        
        #creating AlchemyAPI object
        alchemyapi = AlchemyAPI()
              
        #requesting json response from AlchemyAPI server
        response = alchemyapi.keywords('url', url)
        
        if response['status'] == 'OK':
    

            for keywords in response['keywords']:
                
                #concept object for storing the extracted concept
                keyword = AlchemyStructure.Keyword()
                
                #extracting the keyword
                keyword.setText(keywords['text'])
                
                #extracting the relevance of keyword
                keyword.setRelevance(keywords['relevance'])
                
                #instantiating the sentiment object 
                sentimentObj = AlchemyStructure.Sentiment()
                
                print (keywords['sentiment']['type'])
                #extracting the score of the sentiment associated with the keyword
                if (keywords['sentiment']["type"] == 'neutral'):
                    sentimentObj.setScore("0")
                else:
                    sentimentObj.setScore(keywords["sentiment"]["score"])
                
                #extracting the type of the sentiment associated with the keyword -> positive, negative or neutral
                sentimentObj.setType(keywords['sentiment']['type'])

                #set the sentiment for keyword
                keyword.setSentiment(sentimentObj)

                
                #append the concept into the list of retrieved concepts
                self.keywordsFromUrl.append(keyword)

        else:
            print('Error in keyword tagging call: ', response['statusInfo'])
            
    
    def getKeywordsFromUrl(self,url):
        """method for returning the extracted keywords from given url"""
        self.extractKeywordsFromUrl(url)
        return self.keywordsFromUrl  
    
    
class SentimentExtraction:
    """class for extracting sentiment associated with a document returned by AlchemyAPI call"""
    def __init__(self):
        """constructor for SentimentExtraction class"""
        self.sentimentFromText = None #Sentiment object for containing the sentiment information associated with the provided text
        self.sentimentFromUrl = None #Sentiment object for containing the sentiment information associated with the provided url
    
    def extractSentimentFromText(self,txt):
        """method for extracting the sentiment associated with the text of a document"""
        
        #creating AlchemyAPI object
        alchemyapi = AlchemyAPI()
              
        #requesting json response from AlchemyAPI server
        response = alchemyapi.sentiment('text', txt)
        
        if response['status'] == 'OK':
            
            #getting the sentiment type from the response
            sentimentType = response['docSentiment']['type']
            
            #checking the sentiment type
            if sentimentType == "neutral":
                sentimentScore = 0
            else:
                sentimentScore = response['docSentiment']['score']
            
            #instantiating sentiment object
            self.sentimentFromText = AlchemyStructure.Sentiment()
            
            #set the value for sentiment type    
            self.sentimentFromText.setType(sentimentType)
            
            #set the value for sentiment score
            self.sentimentFromText.setScore(sentimentScore)
            
        else:
            print('Error in sentiment analysis call: ', response['statusInfo'])
            
    def getSentimentFromText(self,txt):
        """method for getting the sentiment information associated with the text"""
        self.extractSentimentFromText(txt)
        return self.sentimentFromText
    
    def extractSentimentFromUrl(self,url):
        """method for extracting the sentiment associated with the url of a document"""
        
        #creating AlchemyAPI object
        alchemyapi = AlchemyAPI()
              
        #requesting json response from AlchemyAPI server
        response = alchemyapi.sentiment('url', url)
        
        if response['status'] == 'OK':
            
            #getting the sentiment type from the response
            sentimentType = response['docSentiment']['type']
            
            #checking the sentiment type
            if sentimentType == "neutral":
                sentimentScore = 0
            else:
                sentimentScore = response['docSentiment']['score']

            #instantiating sentiment object
            self.sentimentFromUrl = AlchemyStructure.Sentiment()

            
            #set the value for sentiment type    
            self.sentimentFromUrl.setType(sentimentType)
            
            #set the value for sentiment score
            self.sentimentFromUrl.setScore(sentimentScore)
            
        else:
            print('Error in sentiment analysis call: ', response['statusInfo'])
            
    def getSentimentFromUrl(self,url):
        """method for getting the sentiment information associated with the text"""
        self.extractSentimentFromUrl(url)
        return self.sentimentFromUrl


class CategoryExtraction:
    """class for extracting the category associated with the given text/url"""
    def __init__(self):
        """constructor for CategoryExtraction"""
        self.categoryFromText = AlchemyStructure.Category()
        self.categoryFromUrl = AlchemyStructure.Category()
        
    def extractCategoryFromText(self,txt):
        """method for extracting the category associated with the given text"""
        
        #creating AlchemyAPI object
        alchemyapi = AlchemyAPI()
              
        #requesting json response from AlchemyAPI server
        response = alchemyapi.category('text', txt)
        
        if response['status'] == 'OK':
            
            #get the category from the response
            self.categoryFromText.setCategory(response['category'])
            
            #get the confidence score from the response
            self.categoryFromText.setScore(response['score'])
            
        else:
            print('Error in text categorization call: ', response['statusInfo'])
            
    
    def getCategoryFromText(self,txt):
        """method for getting the category associated with the provided text"""
        self.extractCategoryFromText(txt)
        return self.categoryFromText
    
    def extractCategoryFromUrl(self,url):
        """method for extracting the category associated with the given url"""
        
        #creating AlchemyAPI object
        alchemyapi = AlchemyAPI()
              
        #requesting json response from AlchemyAPI server
        response = alchemyapi.category('text', url)
        
        if response['status'] == 'OK':
            
            #get the category from the response
            self.categoryFromUrl.setCategory(response['category'])
            
            #get the confidence score from the response
            self.categoryFromUrl.setScore(response['score'])
            
        else:
            print('Error in text categorization call: ', response['statusInfo'])
            
    
    def getCategoryFromUrl(self,url):
        """method for getting the category associated with the provided text"""
        self.extractCategoryFromUrl(url)
        return self.categoryFromUrl
    
    
 
    
    
            
             
        
        


    

    
    


    