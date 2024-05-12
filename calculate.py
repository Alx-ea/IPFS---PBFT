import json

def extract_performance_metrics(filepath):
    # Initialize sums and count
    total_block_creation_time = 0
    total_validation_local_time = 0
    total_validation_total_time = 0
    total_consensus_time = 0
    count = 0
    
    try:
        with open(filepath, 'r') as file:
            for line in file:
                try:
                    block = json.loads(line)
                    stats = block.get("votingStatistics", {})
                    total_block_creation_time += int(stats.get("blockCreationLocalTime", 0))
                    total_validation_local_time += int(stats.get("validationLocalTime", 0))
                    total_validation_total_time += int(stats.get("validationTotalTime", 0))
                    total_consensus_time += int(stats.get("consensusTotalTime", 0))
                    count += 1
                except json.JSONDecodeError as e:
                    print(f"Failed to decode JSON on one of the lines. Error: {e}")
                    # Optionally continue or break, depending on whether you want to skip faulty lines
                    continue
    except FileNotFoundError:
        print("The file was not found. Please check the path and try again.")
        return None

    if count == 0:
        print("No valid data found in the file.")
        return None

    # Calculate averages
    avg_block_creation = total_block_creation_time / count
    avg_validation_local = total_validation_local_time / count
    avg_validation_total = total_validation_total_time / count
    avg_consensus = total_consensus_time / count

    return avg_block_creation, avg_validation_local, avg_validation_total, avg_consensus

def main():
    input_file_path = input("Please enter the path to the input file: ")
    average_stats = extract_performance_metrics(input_file_path)
    
    if average_stats:
        output_file_path = "performance_statistics.txt"
        with open(output_file_path, 'w') as file:
            file.write(f"Average Block Creation Local Time: {average_stats[0]:.2f} ms\n")
            file.write(f"Average Validation Local Time: {average_stats[1]:.2f} ms\n")
            file.write(f"Average Validation Total Time: {average_stats[2]:.2f} ms\n")
            file.write(f"Average Consensus Time: {average_stats[3]:.2f} ms\n")
        
        print(f"Performance statistics written to {output_file_path}")

if __name__ == "__main__":
    main()

