public with sharing class Coral_CLoud_AK_Resort_Manager_LLMMock {

    // Define input parameters
    public class Input {
        @InvocableVariable(required=true label='query' description='String input for the query.')
        public String query;

        @InvocableVariable(required=true label='sample response' description='String input for the expected output that will be echoed back.')
        public String sample_response;
    }

    // Define output parameters
    public class Output {
        @InvocableVariable(label='generatedOutput' description='String ouput for the query based on the sample response.')
        public String generatedOutput;
    }

    // Define the invocable method
    @InvocableMethod(label='Generate Example Output for Coral_CLoud_AK_Resort_Manager' description='This action generates an example output based on the input variables and sample response related to company CoralCLoudAK using the Models API.')
    public static List<Output> generateExampleOutput(List<Input> inputs) {
        List<Output> results = new List<Output>();

        for (Input input : inputs) {
            Output output = new Output();
            // Call the LLM API to generate the example output
            output.generatedOutput = callLLMApi(input.query, input.sample_response);
            results.add(output);
        }

        return results;
    }

    // Method to call the LLM API and generate the example output
    public static String callLLMApi(String query, String sampleResponse) {
        // Create generate text request
        aiplatform.ModelsAPI.createGenerations_Request request = new aiplatform.ModelsAPI.createGenerations_Request();
        request.modelName = 'llmgateway__OpenAIGPT4Omni';

        // Create request body
        aiplatform.ModelsAPI_GenerationRequest requestBody = new aiplatform.ModelsAPI_GenerationRequest();
        request.body = requestBody;

        Date today = Date.today();

        // Construct the prompt for the mock LLM API call
        String prompt = 'Your task is to generate an example output based on provided input variables and a sample output.  The generated example should be realistic response that represents an API response and consistent with the given inputs. \n\n' +
            'Input variables:\n' + query + '\n\n' +
            'Sample Output:\n' + sampleResponse + '\n\n' +
            'To generate a new example output, follow these rules:\n\n' +
            '- The Company that the example output should reflect is CoralCLoudAK \n' +
            '- Generate a new example that expands and adds more detail to the sample output and includes related properties, but with different content that is still realistic and consistent with the input variables.\n' +
            '- Ensure that your generated example incorporates all the input variables in a logical and coherent manner.\n' +
            '- Make sure the generated example is distinct from the sample output\n' +
             '- Always output valid JSON \n' +
            '- If the sample output includes any specific formatting, such as bullet points, numbered lists, or special characters, replicate that formatting in your generated example.\n' +
            '- If dates are expected in the future, use a reasonable date after ' + today + '.\n' +
            '- If dates are expected in the past, use a reasonable date prior to ' + today + '.\n\n';

        // Add prompt to body
        requestBody.prompt = prompt;

        try {
            // Make request
            aiplatform.ModelsAPI modelsAPI = new aiplatform.ModelsAPI();
            aiplatform.ModelsAPI.createGenerations_Response response = modelsAPI.createGenerations(request);

            // Return the generated text from the response
            return response.Code200.generation.generatedText;
        } catch (aiplatform.ModelsAPI.createGenerations_ResponseException e) {
            // Log error and return a default error message
            System.debug('Response code: ' + e.responseCode);
            System.debug('The following exception occurred: ' + e);
            return 'Error generating example output: ' + e.getMessage();
        }
    }
}
