namespace CalculatorTest.Steps
{
    using CalculatorTest.PageObjects;
    using CalculatorTest.Process;
    using NUnit.Framework;
    using TechTalk.SpecFlow;

    [Binding]
    public class InputSteps
    {
        [Given(@"I have entered ([-0-9]+) into the calculator")]
        public void GivenIHaveEnteredIntoTheCalculator(string value)
        {
            var keypad = new KeypadUI(FeatureContext.Current.ProcessId());
            keypad.EnterDigits(value);
        }

        [Given(@"I have pressed add")]
        public void WhenIPressAdd()
        {
            var keypad = new KeypadUI(FeatureContext.Current.ProcessId());
            keypad.EnterDigits("+");
        }

        [When(@"I press equals")]
        public void WhenIPressEquals()
        {
            var keypad = new KeypadUI(FeatureContext.Current.ProcessId());
            keypad.EnterDigits("=");
        }

        [Then(@"the result should be (.+) on the screen")]
        public void ThenTheResultShouldBeOnTheScreen(string expectedResult)
        {
            var keypad = new KeypadUI(FeatureContext.Current.ProcessId());
            var currentResult = keypad.GetResult();
            Assert.AreEqual(expectedResult, currentResult);
        }
    }
}
