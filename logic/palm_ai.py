'''
This file contains the logic for Palm2, which is use to summarize paragraphs.
'''
import google.generativeai as palm
from typing import List
from google.generativeai.types.discuss_types import ChatResponse
import time

class PalmAI:
    def __init__(self, api_key: str) -> None:
        palm.configure(api_key=api_key)
        self.summarize_list = []
        self.ellapsed_time = 0.0
        self.final_summary = ''

    def set_question_prompt(self, text: str) -> None:
        self.__question_prompt_template = '''
                  Please provide a consise summary in 2 short bullets points
                  TEXT: %s
                  SUMMARY:
                  ''' % text

    def set_final_prompt(self) -> None:
        # run through the list of summaries and conclude the final summary
        self.__final_prompt_template = '''
                    Please provide a concise summary in 3 short bullets points for this list of text
                    TEXT_LIST: %s
                    SUMMARY:
                    ''' % self.summarize_list
        
    def partial_summarize(self, text: str) -> None:
        self.set_question_prompt(text)
        
        palm_thread = palm.chat(messages=[self.__question_prompt_template])
        # palm_thread = palm.chat_async(messages=[self.__question_prompt_template])
        self.summarize_list.append(palm_thread.last)

    def final_summarize(self) -> ChatResponse:
        # run through all the summaries and conclude the final summary
        self.set_final_prompt()

        palm_thread = palm.chat(messages=[self.__final_prompt_template])

        return palm_thread.last
    
    def summarize(self, long_text: str) -> None:
        start_time = time.time()
        print('Summarizing...')
        text_list = self.text_breakdown(long_text)

        for text in text_list:
            self.partial_summarize(text)

        print(self.summarize_list)
        print('Summarization complete.')
        end_time = time.time()

        self.final_summary = self.final_summarize()

        self.ellapsed_time = end_time - start_time

    def text_breakdown(self, long_text: str) -> List[str]:
        '''
        Breaks down a long text into smaller chunks of text.
        '''
        output = []
        interval = 512
        if len(long_text) < interval:
            interval = len(long_text)
        for i in range(0, len(long_text), interval):
            output.append(long_text[i:i+interval])

        return output
    
    def save_to_file(self, file_name: str) -> None:
        full_content = ''

        for item in self.summarize_list:
            full_content += item + '\n'

        # final summary
        full_content += '\nFINAL SUMMARY:\n%s' % self.final_summary

        with open(file_name, 'w') as f:
            f.write(full_content)


    def get_elapsed_time(self) -> float:
        return self.ellapsed_time