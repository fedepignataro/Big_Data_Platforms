
public class Tree {

	// By using a static method the Tree class is never instantiated but the processing logic is still abstracted away
	public static String processTree(String line) {

		String[] characteristics = line.split(";");
		String year = characteristics[5];
		String height = characteristics[6];

		// Return the line
		return year + '\t' + height + '\n';
	}
}
