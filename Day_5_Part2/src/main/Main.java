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
            String key = parts[1];  // La page dépendante
            String value = parts[0]; // La page préalable

            instructionsDict.putIfAbsent(key, new HashSet<>());
            instructionsDict.get(key).add(value);
        }

        int total = 0;

        // Sélectionner les mises à jour incorrectement ordonnées
        List<String> incorrectlyOrdered = new ArrayList<>();
        for (String update : updates) {
            String[] updateArray = update.split(",");
            Object[] orderStatus = checkOrder(updateArray, instructionsDict);
            if (!(boolean) orderStatus[0]) {
                incorrectlyOrdered.add(update);
            }
        }

        // Traiter chaque mise à jour incorrecte
        for (String update : incorrectlyOrdered) {
            String[] updateArray = update.split(",");
            Object[] orderStatus;
            String problem;

            // Vérifier l'ordre et réorganiser jusqu'à ce qu'il soit correct
            do {
                orderStatus = checkOrder(updateArray, instructionsDict);
                if (!(boolean) orderStatus[0]) {
                    problem = (String) orderStatus[1]; // récupérer l'erreur
                    String[] problemParts = problem.split(",");
                    updateArray = newOrder(updateArray, problemParts);
                }
            } while (!(boolean) orderStatus[0]);

            int median = Integer.parseInt(updateArray[updateArray.length / 2]);
            total += median;
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

    public static Object[] checkOrder(String[] update, Map<String, Set<String>> instructionsDict) {
        boolean isValid = true;
        String problem = "";

        for (int i = 0; i < update.length; i++) {
            String current = update[i];
            Set<String> prerequisites = instructionsDict.getOrDefault(current, Collections.emptySet());

            for (int j = i + 1; j < update.length; j++) {
                String next = update[j];
                if (prerequisites.contains(next)) {
                    isValid = false;
                    problem = current + "," + next; // Identifier le problème
                    break;
                }
            }
            if (!isValid) break;
        }

        return new Object[] {isValid, problem};
    }

    public static String[] newOrder(String[] update, String[] problem) {
        List<String> updateList = new ArrayList<>(Arrays.asList(update));

        String firstProblem = problem[0];
        String secondProblem = problem[1];

        updateList.remove(secondProblem);
        updateList.add(updateList.indexOf(firstProblem), secondProblem);

        return updateList.toArray(new String[0]);
    }
}
