import torch


def main():
    print("Hello from sturdy-fiesta!")
    # Use CUDA if available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # Use Metal if available
    device = torch.device("mps" if torch.backends.mps.is_available() else device)
    print(f"{device=}")


if __name__ == "__main__":
    main()
