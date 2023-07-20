import { useState } from "react";

const content = [
  {
    tab: "Section 1",
    content: "I'm the content of the Section 1",
  },
  {
    tab: "Section 2",
    content: "I'm the content of the Section 2",
  },
];

const useTabs = (initialTab, allTabs) => {
  const [currentIndex, setCurrentIndex] = useState(initialTab);

  if (!allTabs || !Array.isArray(allTabs)) {
    return;
  }

  return {
    currentItem: allTabs[currentIndex],
    changeItem: setCurrentIndex,
  };
};

function App() {
  const { currentItem, changeItem } = useTabs(1, content);

  return (
    <div>
      <h1>Hello</h1>
      {content.map((section, index) => (
        <button
          onClick={() => {
            changeItem(index);
          }}
          key={index}
        >
          {section.tab}
        </button>
      ))}

      <div>{currentItem.content}</div>
    </div>
  );
}

export default App;
