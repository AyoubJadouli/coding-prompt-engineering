import os
import sys
import chardet

def generate_prompt(directory=None):
  """
  Generates a single prompt representing all the code in a directory,
  including the project tree structure and file contents.

  Args:
    directory: The path to the directory containing the code. 
              If None, the current directory is used.

  Returns:
    A string representing the prompt.
  """

  if directory is None:
    directory = os.getcwd()

  prompt = f"Project tree for directory: {directory}\n\n"

  for root, dirs, files in os.walk(directory):
    level = root.replace(directory, '').count(os.sep)
    indent = ' ' * 4 * level
    prompt += f"{indent}{os.path.basename(root)}/\n"
    subindent = ' ' * 4 * (level + 1)
    for f in files:
      prompt += f"{subindent}{f}\n"
      file_path = os.path.join(root, f)
      
      try:
          # Detect file encoding
          with open(file_path, 'rb') as file:
              raw_data = file.read()
              result = chardet.detect(raw_data)
              encoding = result['encoding']

          # Read file content with detected encoding
          with open(file_path, 'r', encoding=encoding) as file:
              file_content = file.read()

          prompt += f"{subindent}```\n{file_content}\n{subindent}```\n"
      except Exception as e:
          print(f"Error reading file {file_path}: {e}")
          # Handle the error, e.g., skip the file or add a placeholder to the prompt

  return prompt

# Example usage with command-line argument:
if len(sys.argv) > 1:
  directory_path = sys.argv[1]
else:
  directory_path = None

prompt = generate_prompt(directory_path)
print(prompt)
