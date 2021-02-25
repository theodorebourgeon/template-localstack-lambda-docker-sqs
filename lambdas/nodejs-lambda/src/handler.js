exports.handler = async (event) => {
  const response = {
    statusCode: 200,
    body: JSON.stringify({ foo: "bar" }),
  };
  console.log(response);
  return true;
};
