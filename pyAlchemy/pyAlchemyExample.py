'''
Created on Feb 2, 2014

@author: cisstudent
'''

import ProcessAlchemy as pa

demo_txt = "Yesterday dumb Bob destroyed my fancy iPhone in beautiful Denver, Colorado. I guess I will have to head over to the Apple Store and buy a new one."

demo_url = "http://sociallywiredramblings.wordpress.com"


#############################################################################
"""                                                                         #
Example of entity extraction from text and url                              #
"""                                                                         #
#############################################################################


"""
Entity extraction from text
"""
print "###################################################\n"
print "'''Entity extraction from text'''\n"
print "###################################################\n"
entityExtractFromText = pa.EntityExtraction()

entities = entityExtractFromText.getNamedEntitiesFromText(demo_txt)

print "The entities detected from the text: ", demo_txt
print "\n"

if entities == []:
    print "Could not detect any entities"
else:
    for entity in entities:
        print "Entity name: ", entity.getName()
        print "Entity type: ", entity.getType()
        print "Entity sentiment type: ", entity.getSentiment().getType()
        print "Entity sentiment score: ", entity.getSentiment().getScore()
        print "\n------------\n"

       
        
"""
Entity extraction from url
"""

print "###################################################\n"
print "'''Entity extraction from url'''\n"
print "###################################################\n"
entityExtractFromUrl = pa.EntityExtraction()

entities = entityExtractFromUrl.getNamedEntitiesFromUrl(demo_url)

print "The entities detected from the url: ", demo_url
print "\n"

if entities == []:
    print "Could not detect any entities"
else:
    for entity in entities:
        print "Entity name: ", entity.getName()
        print "Entity type: ", entity.getType()
        print "Entity sentiment type: ", entity.getSentiment().getType()
        print "Entity sentiment score: ", entity.getSentiment().getScore()
        print "\n------------\n"
        
        
        
#############################################################################
"""                                                                         #
Example of keyword extraction from text and url                              #
"""                                                                         #
#############################################################################

"""
Keyword extraction from text
"""
print "###################################################\n"
print "'''Keyword extraction from text'''\n"
print "###################################################\n"

print "The keywords detected from the text: ", demo_txt
print "\n"


keywordExtractFromText = pa.KeywordExtraction()

keywords = keywordExtractFromText.getKeywordsFromText(demo_txt)

if keywords == []:
    print "No keywords detected"
else:
    for keyword in keywords:
        print "Keyword: ",keyword.getText()
        print "Keyword Sentiment type: ",keyword.getSentiment().getType()
        print "Keyword Sentiment score: ", keyword.getSentiment().getScore()
        print "\n----------------------\n"
        
        
#"""
#Keyword extraction from url
#"""
#print "###################################################\n"
#print "'''Keyword extraction from url'''\n"
#print "###################################################\n"
#
#keywordExtractFromUrl = pa.KeywordExtraction()
#
#keywords = keywordExtractFromUrl.getKeywordsFromUrl(demo_url)
#
#if keywords == []:
#    print "No keywords detected"
#else:
#    for keyword in keywords:
#        print "Keyword: ",keyword.getText()
#        print "Keyword Sentiment type: ",keyword.getSentiment().getType()
#        print "Keyword Sentiment score: ", keyword.getSentiment().getScore()
#        print "\n----------------------\n"


#############################################################################
"""                                                                         #
Example of concept extraction from text and url                              #
"""                                                                         #
#############################################################################

"""
Concept extraction from text
"""
print "###################################################\n"
print "'''Concept extraction from text'''\n"
print "###################################################\n"

print "The concepts detected from the text: ", demo_txt
print "\n"

conceptExtractFromText = pa.ConceptExtraction()

concepts = conceptExtractFromText.getConceptsFromText(demo_txt)

if concepts == []:
    print "No concepts detected"
else:
    for concept in concepts:
        print "Concept: ",concept.getText()
        print "Concept relevance: ", concept.getRelevance()
        
        print "\n----------------------\n"
        

"""
Concept extraction from url
"""
print "###################################################\n"
print "'''Concept extraction from url'''\n"
print "###################################################\n"

print "The concepts detected from the url: ", demo_url
print "\n"


conceptExtractFromUrl = pa.ConceptExtraction()

concepts = conceptExtractFromUrl.getConceptsFromUrl(demo_url)

if concepts == []:
    print "No concepts detected"
else:
    for concept in concepts:
        print "Concept: ",concept.getText()
        print "Concept relevance: ", concept.getRelevance()
        
        print "\n----------------------\n"


#############################################################################
"""                                                                         #
Example of sentiment extraction from text and url                              #
"""                                                                         #
#############################################################################

"""
Sentiment extraction from text
"""
print "###################################################\n"
print "'''Sentiment extraction from text'''\n"
print "###################################################\n"

print "The sentiment detected from the text: ", demo_txt
print "\n"


sentimentExtractFromText = pa.SentimentExtraction()

sentiment = sentimentExtractFromText.getSentimentFromText(demo_txt)

if sentiment == None:
    print "No sentiments detected"
else:
    
    print "Sentiment Type: ",sentiment.getType()
    print "Sentiment Score: ", sentiment.getScore()
    
    print "\n----------------------\n"
        

"""
Sentiment extraction from url
"""
print "###################################################\n"
print "'''Sentiment extraction from url'''\n"
print "###################################################\n"

print "The sentiment detected from the url: ", demo_url
print "\n"


sentimentExtractFromUrl = pa.SentimentExtraction()

sentiment = sentimentExtractFromUrl.getSentimentFromUrl(demo_url)

if sentiment == None:
    print "No sentiments detected"
else:
    
    print "Sentiment Type: ",sentiment.getType()
    print "Sentiment Score: ", sentiment.getScore()
    
    print "\n----------------------\n"


"""
Category extraction from text
"""
print "###################################################\n"
print "'''Category extraction from text'''\n"
print "###################################################\n"

print "The category detected from the text: ", demo_txt
print "\n"


categoryExtractFromText = pa.CategoryExtraction()

category = categoryExtractFromText.getCategoryFromText(demo_txt)

if category == None:
    print "No category detected"
else:
    
    print "Category: ",category.getCategory()
    print "Category Score: ", category.getScore()
    
    print "\n----------------------\n"
    
"""
Category extraction from text
"""
print "###################################################\n"
print "'''Category extraction from url'''\n"
print "###################################################\n"

print "The category detected from the url: ", demo_url
print "\n"


categoryExtractFromUrl = pa.CategoryExtraction()

category = categoryExtractFromUrl.getCategoryFromUrl(demo_url)

if category == None:
    print "No category detected"
else:
    
    print "Category: ",category.getCategory()
    print "Category Score: ", category.getScore()
    
    print "\n----------------------\n"

        
