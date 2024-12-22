package main;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<String> input = readFile("src/input.txt");
        List<String> instructions = new ArrayList<>();
        List<String> updates = new ArrayList<>();

        for (String line : input) {
            if (line.contains("|")) {
                instructions.add(line);
            } else if (!line.isEmpty()) {
                updates.add(line);
            }
        }
        Map<String, Set<String>> instructionsDict = new HashMap<>();
        for (String instruction : instructions) {
            String[] parts = instruction.split("\\|");
            String key = parts[1];
            String value = parts[0];

            instructionsDict.putIfAbsent(key, new HashSet<>());
            instructionsDict.get(key).add(value);
        }

        int total = 0;
        for (String update : updates) {
            String[] updateArray = update.split(",");
            boolean isValidOrder = checkOrder(updateArray, instructionsDict);

            if (isValidOrder) {
                int median = Integer.parseInt(updateArray[updateArray.length / 2]);
                total += median;
            }
        }
        System.out.println(total);
    }

    public static List<String> readFile(String filePath) {
        List<String> lines = new ArrayList<>();
        try (Scanner scanner = new Scanner(new File(filePath))) {
            while (scanner.hasNextLine()) {
                lines.add(scanner.nextLine());
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        return lines;
    }

    public static boolean checkOrder(String[] update, Map<String, Set<String>> instructionsDict) {
        for (int i = 0; i < update.length; i++) {
            String current = update[i];
            Set<String> prerequisites = instructionsDict.getOrDefault(current, Collections.emptySet());

            for (int j = i + 1; j < update.length; j++) {
                String next = update[j];
                if (prerequisites.contains(next)) {
                    return false;
                }
            }
        }
        return true;
    }
}
