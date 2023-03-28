def print_models(unprinted_designs, completed_models):
    """Simulate printing design until none is left.
        Move each design to completed models after printing
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing Model: {current_design}")
        # Appending the current design
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Display all completed modes"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)