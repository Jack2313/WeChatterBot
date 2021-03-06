from app.chatterbot.logic import LogicAdapter
from app.chatterbot.conversation import Statement

class RulesResponseAdapter(LogicAdapter):
    """
    Return a specific response to a specific input.

    :kwargs:
        * *input_text* (``str``) --
          The input text that triggers this logic adapter.
        * *output_text* (``str``) --
          The output text returned by this logic adapter.
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.chatbot = chatbot


    def can_process(self, statement):
        return True

    def process(self, statement, additional_response_selection_parameters=None):

        rules_list = self.chatbot.storage.filter_rules() # 提取所有规则对话
        response = Statement(text='',confidence=0)
        for rule in rules_list:
            if statement.text == rule.text:
                response = Statement(text=rule.in_response_to)
                response.confidence=10
                break
        return response
