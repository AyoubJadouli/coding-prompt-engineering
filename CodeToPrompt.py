import os

def generate_prompt(directory):
  """
  Generates a single prompt representing all the code in a directory,
  including the project tree structure and file contents.

  Args:
    directory: The path to the directory containing the code.

  Returns:
    A string representing the prompt.
  """

  prompt = f"Project tree for directory: {directory}\n\n"

  for root, dirs, files in os.walk(directory):
    level = root.replace(directory, '').count(os.sep)
    indent = ' ' * 4 * level
    prompt += f"{indent}{os.path.basename(root)}/\n"
    subindent = ' ' * 4 * (level + 1)
    for f in files:
      prompt += f"{subindent}{f}\n"
      file_path = os.path.join(root, f)
      with open(file_path, 'r') as file:
        file_content = file.read()
        prompt += f"{subindent}```\n{file_content}\n{subindent}```\n"

  return prompt

# Example usage:
directory_path = '/path/to/your/code/directory'
prompt = generate_prompt(directory_path)
print(prompt)
