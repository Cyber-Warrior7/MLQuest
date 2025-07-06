import sys
from io import StringIO

def execute_code(code: str) -> str:
    # Basic sandboxed execution: redirect stdout
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        # Warning: using exec; in production, use proper sandbox
        exec(code, {})
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    return output
