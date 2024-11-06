import yaml

with open('../config/config2.yaml', 'r') as file:
    config = yaml.safe_load(file)
    # print(config)
    openai_base = config['llm']['base_url']
    openai_api_key = config['llm']['api_key']
    model_name = config['llm']['model']  # code-davinci-002' # 'text-davinci-002'

    print(openai_api_key, model_name)


# ! pip install openai

import openai
openai.api_base = openai_base
openai.api_key = openai_api_key

def lmp(base_prompt, query, stop_tokens=None, query_kwargs=None):
    new_prompt = f'{base_prompt}\n{query}'

    use_query_kwargs = {
        'engine': model_name,
        'max_tokens': 512,
        'temperature': 0,
    }
    if query_kwargs is not None:
      use_query_kwargs.update(query_kwargs)

    response = openai.Completion.create(
        prompt=new_prompt, stop=stop_tokens, **use_query_kwargs
    )['choices'][0]['text'].strip()

    print(query)
    print(response)

    return response

prompt_pure_python = '''
# Python script
# get the variable a.
ret_val = a
'''.strip()

_ = lmp(prompt_pure_python, '# find the sum of variables a and b.', ['#'])

_ = lmp(prompt_pure_python, '# find the sum of numbers in a list called values.', ['#'])

_ = lmp(prompt_pure_python, '# find the difference between the max and min numbers in a list called xs.', ['#'])

_ = lmp(prompt_pure_python, '# see if any number is divisible by 3 in a list called xs.', ['#'])

prompt_context = '''
objects = ['green block', 'green bowl', 'yellow block', 'yellow bowl']
# the yellow block.
ret_val = 'yellow block'
# the blocks.
ret_val = ['green block', 'yellow block']
'''.strip()

context = "objects = ['blue bowl', 'red block', 'red bowl', 'blue block']"
query = '# the bowls.'

print(context)
_ = lmp(f'{prompt_context}\n{context}', query, ['#', 'objects = ['])

context = "objects = ['blue bowl', 'red block', 'red bowl', 'blue block']"
query = '# sea-colored block.'

print(context)
_ = lmp(f'{prompt_context}\n{context}', query, ['#', 'objects = ['])


context = '''
objects = ['blue bowl', 'red block', 'red bowl', 'blue block']
# sea-colored block.
ret_val = 'blue block'
objects = ['blue bowl', 'red block', 'red bowl', 'blue block']
'''.strip()
query = '# the other block.'

print(context)
_ = lmp(f'{prompt_context}\n{context}', query, ['#', 'objects = ['])

prompt_3lib = '''
import numpy as np
# move all points in pts_np toward the right.
ret_val = pts_np + [0.3, 0]
# move a pt_np toward the top.
ret_val = pt_np + [0, 0.3]
'''.strip()


query = '# get the left most point in pts_np.'

_ = lmp(prompt_3lib, query, ['#'])

query = '# get the center of pts_np.'

_ = lmp(prompt_3lib, query, ['#'])

query = '# the closest point in pts_np to pt_np.'

_ = lmp(prompt_3lib, query, ['#'])

prompt_1lib = '''
from utils import get_pos, put_first_on_second
objects = ['gray block', 'gray bowl']
# put the gray block on the gray bowl.
put_first_on_second('gray block', 'gray bowl')
objects = ['purple block', 'purple bowl']
# move the purple bowl toward the left.
target_pos = get_pos('purple bowl') + [-0.3, 0]
put_first_on_second('purple bowl', target_pos)
'''.strip()

context = "objects = ['blue bowl', 'red block', 'red bowl', 'blue block']"
query = '# move the red block a bit to the right.'

print(context)
_ = lmp(f'{prompt_1lib}\n{context}', query, ['#', 'objects = ['])

context = "objects = ['blue bowl', 'red block', 'red bowl', 'blue block']"
query = '# put the blue block on the bowl with the same color.'

print(context)
_ = lmp(f'{prompt_1lib}\n{context}', query, ['#', 'objects = ['])

prompt_combined = '''
import numpy as np
from utils import get_pos, put_first_on_second
objects = ['cyan block', 'cyan bowl', 'pink bowl']
# put the cyan block in cyan bowl.
put_first_on_second('cyan block', 'cyan bowl')
objects = ['gray block', 'silver block', 'gray bowl']
# place the top most block on the gray bowl.
names = ['gray block', 'silver block']
positions = np.array([get_pos(name) for name in names])
name = names[np.argmax(positions[:,1])]
put_first_on_second(name, 'gray bowl')
objects = ['purple block', 'purple bowl']
# put the purple bowl to the left of the purple block.
target_pos = get_pos('purple block') + [-0.3, 0]
put_first_on_second('purple bowl', target_pos)
'''.strip()

context = "objects = ['red block', 'blue bowl', 'blue block', 'red bowl']"
query = '# move the left most bowl toward the right.'

print(context)
_ = lmp(f'{prompt_combined}\n{context}', query, ['#', 'objects = ['])

context = "objects = ['red block', 'blue bowl', 'blue block', 'red bowl']"
query = '# place the blocks in bowls with their colors.'

print(context)
_ = lmp(f'{prompt_combined}\n{context}', query, ['#', 'objects = ['])

context = "objects = ['red block', 'blue bowl', 'blue block', 'red bowl']"
query = '# move the red block to the middle of the bowls.'

print(context)
_ = lmp(f'{prompt_combined}\n{context}', query, ['#', 'objects = ['])

