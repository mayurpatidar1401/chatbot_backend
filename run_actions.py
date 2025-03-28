from actions.gpt_actions import ActionGPT4Response
from rasa_sdk.executor import ActionExecutor
from rasa_sdk import endpoint

executor = ActionExecutor()
executor.register_action(ActionGPT4Response())

print("✅ Manually registered action_gpt4_response")

endpoint.run(executor, port=5055)
