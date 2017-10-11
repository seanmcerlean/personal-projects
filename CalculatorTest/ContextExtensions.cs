namespace CalculatorTest
{
    using CalculatorTest.Process;
    using TechTalk.SpecFlow;

    public static class ContextExtensions
    {
        public static CalculatorProcess Process(this SpecFlowContext context)
        {
            return context.Get<CalculatorProcess>("Process");
        }

        public static void Process(this SpecFlowContext context, CalculatorProcess process)
        {
            context.Set(process, "Process");
        }

        public static int ProcessId(this SpecFlowContext context)
        {
            return context.Get<int>("ProcessId");
        }

        public static void ProcessId(this SpecFlowContext context, int processId)
        {
            context.Set(processId, "ProcessId");
        }
    }
}
