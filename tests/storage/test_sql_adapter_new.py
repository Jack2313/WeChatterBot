from unittest import TestCase
from app.chatterbot_api.chatterbot.conversation import Statement
from app.chatterbot_api.chatterbot.conversation import StatementRules
from app.chatterbot_api.chatterbot.storage.sql_storage_new import SQLStorageAdapterNew

test = SQLStorageAdapterNew(database_uri='sqlite:///db.sqlite3')
test.drop()
test.create_database()
'''
create rule and statement
'''

test.create_rule(id=1,
                 text="1",
                 in_response_to="2")
test.create_rule(
                 text="How are you?",
                 in_response_to="I'm fine.")
test.create_text(id=1,
                 text="Hello")
test.create_text(id=2,
                 text="Hello!")
test.create_text(text="How are you?")
'''
count rule and statement
'''
statement_count = test.count("statement")
rule_count = test.count("statementrules")
print("stmt count = ",statement_count)
print("rule count = ",rule_count)

'''
filter rule and statement
'''
res=list(test.filter_rules())
print("len=",len(res))

res = list(test.filter_text())
print("res size=",len(res))
if len(res) >0:
    print(res[0].id,res[0].text)
res=list(test.filter_rules(id=1,search_text="hello!"))
if len(res)==0:
    print("Yes")

res=list(test.filter_rules(id=1))
if len(res)==1:
    print("Yes")

'''
update rule and text
'''

test.update_text(Statement(text="I am angry.",in_response_to="too young too simple!"))
res=list(test.filter_text(text="I am angry."))
print(res[0].in_response_to)

test.update_text(Statement(text="I am angry.",in_response_to="sometimes naive!",id=1))
res=list(test.filter_text(text="I am angry."))
print(res[0].in_response_to)

test.update_rule(StatementRules(text="I am angry.",in_response_to="too young too simple!"))
res=list(test.filter_rules(search_text="I am angry."))
#print(res[0].search_in_response_to)

test.update_rule(StatementRules(text="I am angry.",in_response_to="too simple!",id=2))
res=list(test.filter_rules(search_text="I am angry."))
#print(res[0].search_in_response_to)

res=list(test.filter_text(text="How are you?"))
#print("id=",res[0].id)

'''
remove rules and statement
'''

test.remove_rules_by_id(1)
res=list(test.filter_rules(id=1))
print(len(res))
res=list(test.filter_text(id=3))
print("len=",len(res))
test.remove_text_by_text("How are you?")
res=list(test.filter_text(id=3))
print("len=",len(res))



