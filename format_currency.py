import locale

def format_currency(amount: float, symbol: str = '$', grouping: bool = True) -> str:
    """
    Formats a float amount as a standardized currency string.

    Args:
        amount: The monetary value as a float.
        symbol: The currency symbol (e.g., '$', '€', '£').
        grouping: Whether to use thousands separators (e.g., 1,000.00).
    
    Returns:
        A formatted currency string.
    """
    # Set the locale to use for thousands grouping (may require system configuration)
    try:
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    except locale.Error:
        # Fallback if the specific locale is not available
        pass 
    
    # Format the number
    formatted_amount = locale.format_string(
        "%.2f", amount, grouping=grouping
    )
    
    return f"{symbol}{formatted_amount}"

# Example Usage:
# print(format_currency(123456.78))         # Output: $123,456.78
# print(format_currency(99.99, symbol='€'))  # Output: €99.99
# print(format_currency(123456.78, grouping=False)) # Output: $123456.78
