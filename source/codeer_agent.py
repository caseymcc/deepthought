import clang.cindex

#class CppAssistantAgent(AssistantAgent):
class CppAgent:
    DEFAULT_SYSTEM_MESSAGE = """You are a helpful AI assistant."""
    DEFAULT_DESCRIPTION = "A cpp coder who understands the entire project."

    def __init__(
        self,
        name: str,
        project_path: str
    ):
        self.name = name
        self.project_path = project_path

    def find_calls(node, call_graph):
        """
        Recursively find all function calls from the given AST node.
        """

        if node.kind == clang.cindex.CursorKind.CALL_EXPR:
            called_function = node.referenced
            if called_function:
                call_graph[node.lexical_parent.spelling].append(called_function.spelling)

        # Recurse for children of this node
        for child in node.get_children():
            find_calls(child, call_graph)

    def generate_call_tree(source_file):
        index = clang.cindex.Index.create()
        tu = index.parse(source_file)
        call_graph = defaultdict(list)

        for node in tu.cursor.get_children():
            if node.kind == clang.cindex.CursorKind.FUNCTION_DECL:
                find_calls(node, call_graph)

        return call_graph

    def generate_project_call_graph(project_root):
        files = find_cpp_files(project_root)
        call_graph = defaultdict(list)
        for file in files:
            generate_call_tree_for_file(file, call_graph)
        return call_graph


def main():
    CppAgent("CppAgent", "/home/caseymcc/projects/gweni")
    # Initialize the index for indexing the source file
    index = clang.cindex.Index.create()

    # Parse a source file
    tu = index.parse('your_cpp_file.cpp')

    # Function to recursively visit nodes
    def visit_node(node, level=0):
        print('-' * level + node.kind.name, node.spelling)
        for c in node.get_children():
            visit_node(c, level + 1)

    # Visit the nodes in the AST
    visit_node(tu.cursor)

if __name__ == "__main__":
    main()