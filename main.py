import greetings
import generate
import input_and_output


class Main:
    def __init__(self):
        self.greet = greetings

    def main(self):
        self.greet.greet_them()

        data = input("Enter data for QR code: ")
        size = int(input("Enter size (1-40): "))
        error = input("Enter error correction level (L, M, Q, H): ")

        qr_generator = generate.Generate(data, size, error)
        
        # Ask for filename
        output_name = input(
            "Enter output file name (including directory if necessary): "
        )
        
        # Generate and save the QR code as SVG
        qr_generator.generate_qr(output_name)  # Pass the filename directly

        print("QR code saved as SVG:", output_name)


if __name__ == "__main__":
    M = Main()
    M.main()
