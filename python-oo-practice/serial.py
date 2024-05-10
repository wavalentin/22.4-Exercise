"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Make a new serial generator"""

        self.start = self.next = start

    def __repr__(self):
        """Display the starting value"""

        return f"Serial Generator(start={self.start}, next={self.next})"

    def generate(self):
        """Returns next value"""

        self.next += 1
        return self.next - 1

    def reset(self):
        """Resets back to starting value, set at 0"""

        self.next = self.start
        

