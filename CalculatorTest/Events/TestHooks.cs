namespace CalculatorTest.Events
{
    using CalculatorTest;
    using CalculatorTest.PageObjects;
    using CalculatorTest.Process;
    using TechTalk.SpecFlow;

    [Binding]
    public sealed class TestHooks
    {
        [BeforeFeature]
        public static void BeforeFeature()
        {
            var calcProcess = new CalculatorProcess();
            FeatureContext.Current.Process(calcProcess);
            FeatureContext.Current.ProcessId(calcProcess.ProcessId);
        }

        [AfterScenario]
        public static void AfterScenario()
        {
            var keypad = new KeypadUI(FeatureContext.Current.ProcessId());
            keypad.Press("C");
        }

        [AfterFeature]
        public static void AfterFeature()
        {
            var calcProcess = FeatureContext.Current.Process();
            calcProcess.Stop();
        }
    }
}
