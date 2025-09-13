function ListGroup() {
  //components cant return more than one element (cant add header)
  let items = [
    'New York', 'Florida', 'Paris', 'Blah'
  ];
  


  return (
    //fragments
    <>
    <h1> List
        {items.length ===0 && <p>No item found</p>}
        <ul className="list-group">
          {items.map((item) => (
            <li className="List-group-item" 
            key={item}
            onClick={() => console.log("clicked")}>
             {item}
             </li>
            ))}
        </ul>
    </h1>
    </>
  );
}

export default ListGroup;
